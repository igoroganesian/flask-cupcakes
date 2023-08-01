'use strict';
const DEFAULT_URL = 'http://localhost:5001';

const $submitBtn = $('#submitBtn');
const $cupcakeList = $('#cupcakeList');
const $addCupcakeForm = $('$addCupcakeForm');


/* gets all cupcake data from API */

async function getCupcakes() {
  let response = await
    axios.get(DEFAULT_URL + '/api/cupcakes');

  return response.data.cupcakes;
}

function showCupcakeList(cupcakes) {
  //cupcakes = data from getCupcakes
  for (let cupcakeData of cupcakes) {
    console.log(cupcakeData, cupcakes);
    //$ for renderCupcake?
    let $cupcake = renderCupcake(cupcakeData);
    $cupcakeList.append($cupcake);
  }
}


/* generates HTML for individual cupcake */

function renderCupcake(cupcake) {
  return(
      `<div>
        <li>${cupcake.flavor} - ${cupcake.size} - ${cupcake.rating}</li>
        <img class="col-2" src=${cupcake.image_url} alt=${cupcake.flavor}>
      </div>`);
}


async function addCupcake(e) {
  e.preventDefault();

  let flavor = $("#flavorInput").val();
  let size = $("#sizeInput").val();
  let rating = $("#ratingInput").val();
  let imageUrl = $("#imageUrlInput").val();

  const newCupcakeData = await axios.post(DEFAULT_URL + '/api/cupcakes', {
    flavor, size, rating, imageUrl
  });

  const newCupcake = renderCupcake(newCupcakeData);
  $cupcakeList.append(newCupcake);
};

$addCupcakeForm.on("submit", addCupcake)


async function start() {
  const cupcakes = await getCupcakes();
  showCupcakeList(cupcakes);
}

start();
