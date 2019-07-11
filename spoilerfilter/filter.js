

TagsLists = {
    "a": document.getElementsByTagName("a"),
    "p": document.getElementsByTagName("p"),
    "h1": document.getElementsByTagName("h1"),
    "h2": document.getElementsByTagName("h2"),
    "h3": document.getElementsByTagName("h3"),
    "label": document.getElementsByTagName("label"),
    "title": document.getElementsByTagName("title"),
    "span": document.getElementsByTagName("span"),
}


function targetTag(tag, keywords){
    tagsIndex = [];
    for (var i = 0; i < tag.length; i++) {
        for (var x = 0; x < keywords.length; x++ ) {
            if (tag[i].textContent.indexOf(keywords[x]) !== -1){
                console.log(tag[i].textContent)
                tagsIndex.push(i)
            };
        };
    };
    return tagsIndex
}

TagsIndex = {
    "a": targetTag(TagsLists["a"],searchText),
    "p": targetTag(TagsLists["p"],searchText),
    "h1":targetTag(TagsLists["h1"],searchText),
    "h2":targetTag(TagsLists["h2"],searchText),
    "h3":targetTag(TagsLists["h3"],searchText),
    "label":targetTag(TagsLists["label"],searchText),
    "title":targetTag(TagsLists["title"],searchText),
    "span":targetTag(TagsLists["span"],searchText)
}



function bluring(tag) {
    var list = TagsIndex[tag];
    var targettag = TagsLists[tag];
    for(i=0; i < list.length; i++){
        targettag[list[i]].style.filter = "blur(5px)"
        targettag[list[i]].parentElement.style.filter = "blur(5px)";
        targettag[list[i]].parentElement.parentElement.parentElement.style.filter = "blur(5px)";
    }
}

export default bluring