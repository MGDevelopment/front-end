<!-- JavaScript bottom -->>
<script type="text/javascript" src="/jquery/jquery.min.js"></script>
<script type="text/javascript" src="/js/popups.js"></script>
<!-- script type="text/javascript" src="/js/equalcolumnsInicio.js"></script>
<script type="text/javascript" src="/js/buscador.js"></script>
<script type="text/javascript" src="/js/jsutil.js"></script>
<script type="text/javascript" src="/js/carritoNew.js"></script>
<script type="text/javascript" src="/js/popups.js"></script>
<script type="text/javascript" src="/js/hashtable.js"></script-->

<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-635166-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script');
    ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(ga, s);
  })();
</script>
	
<script type="text/javascript">
	//<![CDATA[ 
	$(document).ready(function(){
		//verificarFiltros();
		aux = '#ctrlDisabled';
		$(aux).get(0).style.display="none";
	});
	//]]>
</script>
<script type="text/javascript">
	//<![CDATA[ 
	var idsCat = new Array();
	var catLibro = 1,catPasatiempo = 3,catMusica = 4,catPelicula = 5;
	var tamView = new Array();
	idsCat[0]=catLibro; 
	idsCat[1]=catPasatiempo;
	idsCat[2]=catMusica;
	idsCat[3]=catPelicula;
	tamView[catLibro]= 4;
	tamView[catPasatiempo]=4;
	tamView[catMusica]=6;
	tamView[catPelicula]=4;
	//]]>
</script>

<!-- New Scripts -->
<script type="text/javascript" src="/js/tematika.js"></script>
<script type="text/javascript" src="/js/comments.js"></script>
<script type="text/javascript" src="home-comments.js"></script>
<script type="text/javascript" src="/js/messages.js"></script>
<script type="text/javascript" src="home-messages.js"></script>
<script type="text/javascript" src="/js/showcase.js"></script>
<script type="text/javascript" src="home-showcase.js"></script>
<script type="text/javascript" src="home-tooltip.js"></script>
<script type="text/javascript" src="/js/home.js"></script>
<!-- Scripts por herencia -->
<script type="text/javascript" src="/js/dropDownMenu.js"></script>
<!-- JQuery Carousel -->
<script type="text/javascript" src="/carousel/jquery.tinycarousel.js"></script>
<script type="text/javascript" src="/carousel/jquery.colorbox.js"></script>
<script type="text/javascript">

jQuery(document).ready(function() {
	$('#sliderHomeBooks').tinycarousel({ axis: 'y', display: 1} );
	$('#sliderHomeMusic').tinycarousel({ axis: 'y', display: 1} );
	$('#sliderHomeMovies').tinycarousel({ axis: 'y', display: 1} );
	$('#sliderHomeGames').tinycarousel({ axis: 'y', display: 1} );
	$(".inline").colorbox({opacity: 0, inline:true, width:"400px"});
	//.bind("mouseover", function(){$(this).trigger("click"); 
});

</script>

