/* comments.js */
function fillComments(section, callback) {
    var commentsHTML = '';
    var defaultSection = 'last';
    
    if (section == null) {
        section = defaultSection;
    }
    
    try {
        if (section != null && TMK.getData('comments')[section]) {
            commentsHTML = TMK.getData('comments')[section];
        }
    } catch (e) {
        commentsHTML = 'Sin comentarios';
    }
    document.getElementById('comments_detail').innerHTML = commentsHTML;
    
    try {
        if (callback && typeof (callback) === "function") {
            // execute the callback, passing parameters as necessary
            callback(section);
        }
    } catch (e) {
        // TODO: handle exception
    }
    return;
}
