import bluring from filter.js

// Replace ./data.json with your JSON feed
fetch('./data.json').then(response => {
    return response.json();
  }).then(data => {
    // Work with JSON data here


if(window.location.href.indexOf("facebook") != -1){
    bluring("a");
    bluring("p");
}

if(window.location.href.indexOf("google") != -1){
    bluring('a');
    bluring('p');
    bluring('span');
}

// if(window.location.href.indexOf("instagram") != -1){
// 	var divTags = document.getElementsByTagName("div");
// 	var pTags = document.getElementsByTagName("p");
// 	var spanTags = document.getElementsByTagName("span");
// var searchText = "am";

// for (var i = 0; i < spanTags.length; i++) {
//     if (spanTags[i].textContent.indexOf(searchText) !== -1){
//         console.log(spanTags[i].textContent);
//         spanTags[i].style.filter = "blur(10px)";
// 		spanTags[i].parentElement.style.filter = "blur(10px)";
// 		spanTags[i].parentElement.parentElement.parentElement.style.filter = "blur(10px)";
//     }
// }
// }

if(window.location.href.indexOf("reddit") != -1){
    bluring("h2").bluring("h2")
}


console.log(data);
}).catch(err => {
  // Do something for an error here
});
