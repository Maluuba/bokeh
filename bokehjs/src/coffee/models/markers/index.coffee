import {Marker, MarkerView} from "./marker"

SQ3 = Math.sqrt(3)

_one_x =  (ctx, r) ->
  ctx.moveTo(-r,  r)
  ctx.lineTo( r, -r)
  ctx.moveTo(-r, -r)
  ctx.lineTo( r,  r)
  return { x: -r, y: -r, w: 2*r, h: 2*r}

_one_cross = (ctx, r) ->
  ctx.moveTo( 0,  r)
  ctx.lineTo( 0, -r)
  ctx.moveTo(-r,  0)
  ctx.lineTo( r,  0)
  return { x: -r, y: -r, w: 2*r, h: 2*r}

_one_diamond = (ctx, r) ->
  ctx.moveTo(0, r)
  ctx.lineTo(r/1.5, 0)
  ctx.lineTo(0, -r)
  ctx.lineTo(-r/1.5, 0)
  ctx.closePath()
  return { x: -r/1.5, y: -r, w: (2*r)/1.5, h: 2*r}

_one_tri = (ctx, r) ->
  h = r * SQ3
  a = h/3

  # TODO (bev) use viewstate to take y-axis inversion into account
  ctx.moveTo(-r, a)
  ctx.lineTo(r, a)
  ctx.lineTo(0, a-h)
  ctx.closePath()
  return { x: -r, y: a-h, w: 2*r, h: a+h}

asterisk = (ctx, i, sx, sy, r, line, fill) ->
  r2 = r*0.65

  bbox = _one_cross(ctx, r)
  _one_x(ctx, r2)

  if line.doit
    line.set_vectorize(ctx, i)
    ctx.stroke()

  return bbox

circle_cross = (ctx, i, sx, sy, r, line, fill)  ->
  ctx.arc(0, 0, r, 0, 2*Math.PI, false)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    _one_cross(ctx, r)
    ctx.stroke()

  return {x: -r, y: -r, w: 2*r, h: 2*r}

circle_x = (ctx, i, sx, sy, r, line, fill) ->
  ctx.arc(0, 0, r, 0, 2*Math.PI, false)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    _one_x(ctx, r)
    ctx.stroke()

  return {x: -r, y: -r, w: 2*r, h: 2*r}

cross = (ctx, i, sx, sy, r, line, fill) ->
  bbox = _one_cross(ctx, r)

  if line.doit
    line.set_vectorize(ctx, i)
    ctx.stroke()

  return bbox

diamond = (ctx, i, sx, sy, r, line, fill) ->
  bbox = _one_diamond(ctx, r)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    ctx.stroke()

  return bbox

diamond_cross = (ctx, i, sx, sy, r, line, fill) ->
  bbox = _one_diamond(ctx, r)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    _one_cross(ctx, r)
    ctx.stroke()

  return bbox

inverted_triangle = (ctx, i, sx, sy, r, line, fill) ->
  ctx.rotate(Math.PI)
  bbox = _one_tri(ctx, r)
  ctx.rotate(-Math.PI)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    ctx.stroke()

  return bbox

square = (ctx, i, sx, sy, r, line, fill) ->
  size = 2*r
  ctx.rect(-r, -r, size, size)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    ctx.stroke()

  return {x: -r, y: -r, w: size, h: size}

square_cross = (ctx, i, sx, sy, r, line, fill) ->
  size = 2*r
  ctx.rect(-r, -r, size, size)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    _one_cross(ctx, r)
    ctx.stroke()

  return {x: -r, y: -r, w: size, h: size}

square_x = (ctx, i, sx, sy, r, line, fill) ->
  size = 2*r
  ctx.rect(-r, -r, size, size)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    _one_x(ctx, r)
    ctx.stroke()

  return {x: -r, y: -r, w: size, h: size}

triangle = (ctx, i, sx, sy, r, line, fill) ->
  bbox = _one_tri(ctx, r)

  if fill.doit
    fill.set_vectorize(ctx, i)
    ctx.fill()

  if line.doit
    line.set_vectorize(ctx, i)
    ctx.stroke()

  return bbox

x = (ctx, i, sx, sy, r, line, fill) ->
  bbox = _one_x(ctx, r)

  if line.doit
    line.set_vectorize(ctx, i)
    ctx.stroke()

  return bbox

_mk_model = (type, f) ->
  class view extends MarkerView
    _render_one: f

  class model extends Marker
    default_view: view
    type: type

  return model

# markers are final, so no need to export views
export Asterisk         = _mk_model('Asterisk',         asterisk)
export CircleCross      = _mk_model('CircleCross',      circle_cross)
export CircleX          = _mk_model('CircleX',          circle_x)
export Cross            = _mk_model('Cross',            cross)
export Diamond          = _mk_model('Diamond',          diamond)
export DiamondCross     = _mk_model('DiamondCross',     diamond_cross)
export InvertedTriangle = _mk_model('InvertedTriangle', inverted_triangle)
export Square           = _mk_model('Square',           square)
export SquareCross      = _mk_model('SquareCross',      square_cross)
export SquareX          = _mk_model('SquareX',          square_x)
export Triangle         = _mk_model('Triangle',         triangle)
export X                = _mk_model('X',                x)
