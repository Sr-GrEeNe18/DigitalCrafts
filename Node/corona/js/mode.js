var container = document.querySelector('container-fluid')

// var homeAnchor = document.createAttribute.element('a')

homeAnchor.textContent = 'Home'
homeAnchor.setAttribute('class', "navbar navbar-expand-lg bg-blue");

function createAnchor(url, text, css){

    var anchor = document.createElement('a')
    anchor.setAttribute('class', css)
    anchor.setAttribute('href', url)
    anchor.textContent = text;

    return anchor
}

var highAnchor = createAnchor("#", "High on Coding", "navbar-brand")
var catAnchor = createAnchor("#", "Categories", "nav-link")
var homeAnchor = createAnchor("#", "Home", "nav-link active")

nav.append(highAnchor);
nav.append(catAnchor);
nav.append(homeAnchor);

function createDiv(css, text){

    var div = document.createElement('div')
    div.setAttribute('class', css)
    div.setAttribute('text', text)
    div.textContent = text;

    return div

}

var row = createDiv('row bg-lgray ml-15 mr-300');

var rowdiv = createDiv('col bg-secondary, "Curse of the Curren Reviews');
var rowdiv1 = createDiv("", "When you want to buy any application from the Apple iTunes store you have more choices than you can handle. Most of the users scroll past the application description comletely avoding it like ads displayed on the right column of your webpage. Their choice is dependent on three important factors price, sceeenshot and reviews.");

row.append(rowdiv)
row.append(rowdiv1)


var row2 = createDiv('row2 mb-4');

var row2div1 = createDiv('row h5 color deepskyblue', "Hello Watchkit");
var row2div2 = creatDiv('Last month Apple released the anticipated WatchKit Framwork for developers in the fom of iOS 8.2 beta SDK release. The WatchKit framework enalble the developers to create Apple Watch applications. In this aricle we are going to focus on the basics of getting started with the WatchKit framework and developing apps fo the Apple Watch.');
var row2div3 = createDiv('row background-color darkorange ml-27 mr-305');
    var r2d3h = createDiv('12 comments', '124 likes');

    row2div3.append(r2d3h);

row2.append(row2div1);
row2.append(row2div2);
row2.append(row2div3);

var row3 = createDiv('row3');

var row3div1 = createDiv('row h5 color deepskyblue', "Introduction to Swift");
var row3div2 = createDiv('Swift is a moder programmin language developed by Apple to create the next generation of iOS ans OSX applications. Swift is a fairly new language and still in development but it clearlu reflects the intentions and the fuuture direction. This article will revolve around the basic concepts in the Swift language an how you can get started.');
var row3div3 = createDiv('row background-color darkorange ml-27 mr-305');
    var r3d3h = createDiv('15 comments', '45 likes');

row3.append(row3div1);
row3.append(row3div2);
row3.append(row3div3);
