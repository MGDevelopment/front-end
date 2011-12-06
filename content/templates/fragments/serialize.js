/**
 * serialize.js
 */
//var serializer = new ONEGEEK.GSerializer();

function _serialize(obj) {
	return JFather.serialize(obj);
	//return serializer.serialize(obj, 'objectName');
}

function _unserialize(obj) {
	return JFather.unserialize(obj);
	//return serializer.deserialize(obj);
}