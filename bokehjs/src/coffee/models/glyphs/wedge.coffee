import {XYGlyph, XYGlyphView} from "./xy_glyph"
import * as hittest from "core/hittest"
import * as p from "core/properties"
import {angle_between} from "core/util/math"
import * as _ from "lodash"

export class WedgeView extends XYGlyphView

  _map_data: () ->
    if @model.properties.radius.units == "data"
      @sradius = @sdist(@renderer.xscale, @_x, @_radius)
    else
      @sradius = @_radius

  _render: (ctx, indices, {sx, sy, sradius, _start_angle, _end_angle}) ->
    direction = @model.properties.direction.value()
    @data =
      name: @renderer.model.name
      model_id: @model.id
      data_fields: ["slices"]
      slices: []

    # assumes 'direction' is always CCW 
    get_slice_bbox = (centre_x, centre_y, rad, start_theta, end_theta) ->
      start_theta *= -1
      end_theta *= -1

      if end_theta - start_theta >= Math.PI
        return { x: centre_x - rad, y: centre_y - rad, w: 2*rad, h: 2*rad }

      # Need to flip implictly because of canvas vs cartesian plane Y direction
      # Also rotate clockwise (i.e. -theta) instead
      cart_x1 = rad*Math.cos(-start_theta)
      cart_y1 = rad*Math.sin(-start_theta)

      cart_x2 = rad*Math.cos(-end_theta)
      cart_y2 = rad*Math.sin(-end_theta)

      # Now need to correct as the arc passes across quadrants (in CW direction bc -ve angles)
      origin_bounding_xs = [0, cart_x1, cart_x2]
      origin_bounding_ys = [0, cart_y1, cart_y2]

      theta = -start_theta
      last_quadrant = null

      # For quadrants, increases in CCW order. Concretely,
      # TR = 0, TL = 1, BL = 2 , BR = 3

      if theta > - Math.PI / 2
        theta = - Math.PI / 2
        last_quadrant = 3
      else if theta > - Math.PI
        theta = - Math.PI
        last_quadrant = 2
      else if theta > - 3 * Math.PI / 2
        theta = - 3 * Math.PI / 2
        last_quadrant = 1
      else
        theta = 0
        last_quadrant = 0

      # if the theta > -end_theta condition isn't satsified, the arc is montonic
      # and the bounding box will be defined by the ray intersections of the arc

      while theta > -end_theta
        switch last_quadrant
          when 3 then origin_bounding_ys.push(-rad)
          when 2 then origin_bounding_xs.push(-rad)
          when 1 then origin_bounding_ys.push(rad)
          when 0 then origin_bounding_xs.push(rad)

        if last_quadrant > 0
          last_quadrant = (last_quadrant - 1) % 4
        else
          last_quadrant = 0
        theta -= Math.PI / 2

      bounding_xs = []
      for i in [0...origin_bounding_xs.length]
        bounding_xs.push(origin_bounding_xs[i] + centre_x)

      bounding_ys = []
      for i in [0...origin_bounding_ys.length]
        bounding_ys.push(origin_bounding_ys[i] + centre_y)

      bbox_x = Math.round(_.min(bounding_xs))
      bbox_y = Math.round(_.min(bounding_ys))

      return { x: bbox_x, y: bbox_y, w: Math.round(_.max(bounding_xs)) - bbox_x, h: Math.round(_.max(bounding_ys)) - bbox_y }

    for i in indices
      if isNaN(sx[i]+sy[i]+sradius[i]+_start_angle[i]+_end_angle[i])
        continue

      ctx.beginPath()
      ctx.arc(sx[i], sy[i], sradius[i], _start_angle[i], _end_angle[i], direction)
      ctx.lineTo(sx[i], sy[i])
      ctx.closePath()
      
      if @visuals.fill.doit
        @visuals.fill.set_vectorize(ctx, i)
        ctx.fill()

      if @visuals.line.doit
        @visuals.line.set_vectorize(ctx, i)
        ctx.stroke()

      span = -(_end_angle[i] - _start_angle[i])*180/Math.PI
      @data.slices.push({ bbox: get_slice_bbox(sx[i], sy[i], sradius[i], _start_angle[i], _end_angle[i]), span: span })

    console.log("render wedge")
    console.log(@)
    window.localStorage.setItem(@data.name, JSON.stringify(@data))

  _hit_point: (geometry) ->
    [vx, vy] = [geometry.vx, geometry.vy]
    x = @renderer.xscale.invert(vx, true)
    y = @renderer.yscale.invert(vy, true)

    # check radius first
    if @model.properties.radius.units == "data"
      x0 = x - @max_radius
      x1 = x + @max_radius

      y0 = y - @max_radius
      y1 = y + @max_radius

    else
      vx0 = vx - @max_radius
      vx1 = vx + @max_radius
      [x0, x1] = @renderer.xscale.v_invert([vx0, vx1], true)

      vy0 = vy - @max_radius
      vy1 = vy + @max_radius
      [y0, y1] = @renderer.yscale.v_invert([vy0, vy1], true)

    candidates = []

    bbox = hittest.validate_bbox_coords([x0, x1], [y0, y1])
    for i in @index.indices(bbox)
      r2 = Math.pow(@sradius[i], 2)
      sx0 = @renderer.xscale.compute(x, true)
      sx1 = @renderer.xscale.compute(@_x[i], true)
      sy0 = @renderer.yscale.compute(y, true)
      sy1 = @renderer.yscale.compute(@_y[i], true)
      dist = Math.pow(sx0-sx1, 2) + Math.pow(sy0-sy1, 2)
      if dist <= r2
        candidates.push([i, dist])

    direction = @model.properties.direction.value()
    hits = []
    for [i, dist] in candidates
      sx = @renderer.plot_view.canvas.vx_to_sx(vx)
      sy = @renderer.plot_view.canvas.vy_to_sy(vy)
      # NOTE: minus the angle because JS uses non-mathy convention for angles
      angle = Math.atan2(sy-@sy[i], sx-@sx[i])
      if angle_between(-angle, -@_start_angle[i], -@_end_angle[i], direction)
        hits.push([i, dist])

    return hittest.create_1d_hit_test_result(hits)

  draw_legend_for_index: (ctx, x0, x1, y0, y1, index) ->
    @_generic_area_legend(ctx, x0, x1, y0, y1, index)

export class Wedge extends XYGlyph
  default_view: WedgeView

  type: 'Wedge'

  @mixins ['line', 'fill']
  @define {
      direction:    [ p.Direction,   'anticlock' ]
      radius:       [ p.DistanceSpec             ]
      start_angle:  [ p.AngleSpec                ]
      end_angle:    [ p.AngleSpec                ]
    }
