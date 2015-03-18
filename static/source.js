/* npm install virtual-dom html-to-vdom domready vdom-virtualize
 * browserify source.js -o bundle.js
 */
var domready = require('domready');
var VNode = require('virtual-dom/vnode/vnode');
var VText = require('virtual-dom/vnode/vtext');

var h = require('virtual-dom/h');
var diff = require('virtual-dom/diff');
var patch = require('virtual-dom/patch');


var convertHTML = require('html-to-vdom')({
    VNode: VNode,
    VText: VText
});

var createElement = require('virtual-dom/create-element');
var virtualize = require('vdom-virtualize');

domready(function(){
	var initialHTML = virtualize(document.body);
	
	global.nagare_vdom_result = function(id, html) {
		var vtree = convertHTML({
		    getVNodeKey: function (attributes) {
		        return attributes.id;
		    }
		}, '<body>' + html + '</body>');
		var _patch = diff(initialHTML, vtree);
	    patch(document.body, _patch);
	    initialHTML = vtree;
	}
	
	global.nagare_loadAll = function(){};
	
});