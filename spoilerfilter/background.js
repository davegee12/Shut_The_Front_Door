chrome.runtime.sendMessage({
    msg: "something_completed", 
    data: {
        subject: "Loading",
        content: "Just completed!"
    }
});




// fetch('http://localhost:8000/filter/request').then(response => {
//     return response.json()
// }).then(data => {
//     chrome.runtime.sendMessage({'targetlist': data["master_list"]})
// });


    // list = json["master_list"];
    // console.log(list);
