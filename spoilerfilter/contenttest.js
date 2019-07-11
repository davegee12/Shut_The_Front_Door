
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        alert("test3")
        if (request.msg === "something_completed") {
            alert("thisis gay")
            console.log(request.data.subject)
            console.log(request.data.content)
        }
    }
);
