/*popups.js*/
function mostrarDiv(id){
	if(document.getElementById(id).style.display== "none"){
		document.getElementById(id).style.display = "block";
		document.getElementById(id).style.visibility='visible'
	}else{
		document.getElementById(id).style.display = "none";
		document.getElementById(id).style.visibility='hidden'
	}
}
function MM_showHideLayers() {
	var i,p,v,obj,args=MM_showHideLayers.arguments;
	for (i=0; i<(args.length-2); i+=3)
		with (document)
			if(getElementById && ((obj=getElementById(args[i]))!=null)){
				v=args[i+2];
				if (obj.style){
					obj=obj.style; 
					v=(v=='show')?'visible':(v=='hide')?'hidden':v; 
				}
				obj.visibility=v;
			}
}