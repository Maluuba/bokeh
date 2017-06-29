function polarToCartesian(radius: number, angle: number): Object {
    return { x: radius * Math.cos(angle), y: radius * Math.sin(angle) };
}

function cartesianToPolar(x: number, y: number): Object {
    return { radius: Math.sqrt( Math.pow(x, 2) + Math.pow(y, 2) ),
             angle: Math.atan(y / x) };
}

function rotateBox(box: Object, delta: number): Object {
    let rotatedBox: Object = {};
    let angles: Array<number> = [];
    for (let key in box) {
        let x: number = box[key].x;
        let y: number = box[key].y;
        let cartCoords: any = cartesianToPolar(x, y);
        let radius: number = cartCoords.radius; 
        let angle: number = cartCoords.angle;
        for (let a of angles) {
            if (a === angle) {
                angle = angle + Math.PI;
                break;
            }
        }
        angles.push(angle);
        rotatedBox[key] = polarToCartesian(radius, angle + delta);
    }
    return rotatedBox;
}

// Rotates about the center of the bbox
export function rotateBboxInPlace(bbox: any, angle = 0): Object {

    // Move to origin
    let boxOrigin: any = { 
        tr: { x: -bbox.w/2, y: bbox.h/2 },
        tl: { x: bbox.w/2,  y: bbox.h/2 },
        bl: { x: -bbox.w/2, y: -bbox.h/2 },
        br: { x: bbox.w/2,  y: -bbox.h/2 }
    };

    // Rotate the box about the origin
    let rotatedBoxOrigin = rotateBox(boxOrigin, angle);

    // Move the box back to where it's supposed to be and align it with the centre draw x & y
    let rotatedBox: Object = {};
    for (let key in rotatedBoxOrigin){
        let ox: number = rotatedBoxOrigin[key].x;
        let oy: number = rotatedBoxOrigin[key].y;
        rotatedBox[key] = {x: ox + bbox.w/2 + bbox.x, y: oy + bbox.h/2 + bbox.y};
    }

    // Finally get the new bounds of the updated bounding box
    // I'd use lodash here but the typescript compiler keeps complaining
    let minX: number = Number.POSITIVE_INFINITY;
    let maxX: number = Number.NEGATIVE_INFINITY;
    let minY: number = Number.POSITIVE_INFINITY;
    let maxY: number = Number.NEGATIVE_INFINITY;
    let curX: number;
    let curY: number;
    for (let key in rotatedBox){
        curX = rotatedBox[key].x;
        curY = rotatedBox[key].y;
        if (curX > maxX) maxX = curX;
        if (curX < minX) minX = curX;
        if (curY > maxY) maxY = curY;
        if (curY < minY) minY = curY;
    }
    let data: any = {x: minX, y: minY, w: maxX - minX, h: maxY - minY};

    return {x: Math.round(data.x), y: Math.round(data.y), w: Math.round(data.w), h: Math.round(data.h)};
}

// Angle must be given in radians
export function getLabelBbox(label: string, ctx: any, x: number, y: number, angle = 0): Object {
    let metrics = ctx.measureText(label);
    let bbox: any = {
        x: x - (metrics.width / 2), // since text is centre aligned by default
        y: y,
        w: metrics.width,
        h: metrics.ascent,
    };
    return rotateBboxInPlace(bbox, angle);
};
