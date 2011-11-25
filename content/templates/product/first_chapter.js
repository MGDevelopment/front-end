/**
 * Name:
 * 	- fisrt_chapter.js
 *
 * HTML dependecy:
 *			<div class="dSolapas" id="primerCap">
 *				<div class="tmtkMesaMenuMod"><div class="solapasTitprimerCap" title="Primer cap’tulo"/></div></div>
 *				<div class="dResena" id="divPrimerCapitulo" style="border:thin solid;border-color: white;"></div>
 *			</div>
 */

var chapter_url = '/asociadas/capitulos/';

function loadFirstChapter() {
	try {
		$('#divPrimerCapitulo').load(chapter_url + '{{ ArticleId }}', function(response, status, xhr) {
            if (status == "error") {
               $("#primerCap").hide();
           }
       });
	} catch (e) {
		// TODO: handle exception
	}
}

loadFirstChapter();