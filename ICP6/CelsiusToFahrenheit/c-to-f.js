module.exports = function(RED) {
    function LowerCaseNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            msg.payload = Math.round(msg.payload * 9 / 5 + 32);
            node.send(msg);
        });
    }
    RED.nodes.registerType("c-to-f",LowerCaseNode);
}