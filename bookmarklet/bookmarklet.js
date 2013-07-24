javascript:(function(){

if (typeof jQuery=='undefined'){
    var script = document.createElement('script');
    script.src = 'http://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js';
    script.onload = main();
    document.body.appendChild(script);
    console.log('Loaded jQuery yo');
}
else{
    main();
}

function main(){
    function run(){
        var selection = window.getSelection();
        if (selection.isCollapsed) 
            return;
        
        var anntStartIndex = getAnntStartIndex();
        alert(anntStartIndex);
        console.log("The annotation start index is " + anntStartIndex);
        
        var anntText = prompt("Spit it out");
        
        $.post('http://127.0.0.1:6543/annotate',
               {data: anntText},
               function resultHandler(data){
                    var fileName = data.fileName;
                    alert("The filename is: " + fileName);
        },"json");
        
        function getAnntStartIndex(){
            var startNode = selection.getRangeAt(0).startContainer;
            var indexWithinNode = selection.getRangeAt(0).startOffset;
             
            var walker = document.createTreeWalker(
                document.body,
                NodeFilter.SHOW_TEXT,
                null,
                false
            );
            
            var textNodes = [];
            var anntStartIndex = 0;
            
            while (node = walker.nextNode()){
                if (node == startNode){
                    break;
                }
                textNodes.push(node);
                anntStartIndex += node.length;
            }
            anntStartIndex += indexWithinNode;
            
            return anntStartIndex;
        }
    }
    document.onmouseup = run;
}

})();
