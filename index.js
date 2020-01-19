let data = [
  {
    name: "banana",
    date: "12/13/2019",
    quantity: "8",
    calories: "420",
    pic:
      "https://media.istockphoto.com/photos/banana-picture-id636739634?k=6&m=636739634&s=612x612&w=0&h=BQ9Z6DobjFzclh3LN7nKSljrRqycJPCq65CS8rtUHU4="
  },
  {
    name: "carrot",
    date: "08/12/2019",
    quantity: "12",
    calories: "642",
    pic: "https://i5.walmartimages.ca/images/Enlarge/271/747/6000191271747.jpg"
  },
  {
    name: "grapefruit",
    date: "01/31/2020",
    quantity: "3",
    calories: "825",
    pic: "https://cdn.britannica.com/22/122522-050-6CD1C3E7/Grapefruit.jpg"
  },
  {
    name: "cake",
    date: "05/07/2020",
    quantity: "1",
    calories: "163",
    pic:
      "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2012/12/20/0/FNM_010113-Smores-Cake-Recipe_s4x3.jpg.rend.hgtvcom.826.620.suffix/1371611980872.jpeg"
  },
  {
    name: "orange",
    date: "11/16/2019",
    quantity: "10",
    calories: "167",
    pic: "https://sites.psu.edu/lifeitmoveson/files/2017/10/orange-1hoca2l.jpg"
  },
  {
    name: "flank_steak",
    date: "11/17/2020",
    quantity: "3",
    calories: "943",
    pic:
      "https://images-na.ssl-images-amazon.com/images/I/71mcO05XVKL._SL1500_.jpg"
  },
  {
    name: "pizza",
    date: "08/26/2020",
    quantity: "1",
    calories: "1230",
    pic:
      "https://storage.pizzapizza.ca/phx2/ppl_images/category/en/2x/old_school.png"
  },
  {
    name: "noodles",
    date: "09/15/2020",
    quantity: "8",
    calories: "445",
    pic:
      "https://upload.wikimedia.org/wikipedia/commons/7/73/Mama_instant_noodle_block.jpg"
  }
];

Handlebars.registerHelper("expire", function(date_arg) {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, "0");
  var mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!
  var yyyy = today.getFullYear();

  today = mm + "/" + dd + "/" + yyyy;
  return new Date(date_arg.date) <= new Date(today);
});
const replaceHTMLProductTemplate = () => {
  let source = document.getElementById("product-template").innerHTML;
  let template = Handlebars.compile(source);
  let context = { data: data };
  let html = template(context);
  document.getElementById("content-placeholder").innerHTML = html;
};

replaceHTMLProductTemplate();
