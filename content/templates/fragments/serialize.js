/**
 * serialize.js
 */

function _serialize(obj) {
    //return JFather.serialize(obj);
    return JSON.stringify(obj);
}

function _unserialize(obj) {
    //return JFather.unserialize(obj);
    return JSON.parse(obj);
}