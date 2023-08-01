'use strict';
const DEFAULT_URL = 'http://localhost:5001';

const $submitBtn = $('#submitBtn');
const $cupcakes = $('#cupcakes');




$submitBtn.on('click', function (e) {
  e.preventDefault();

});

async function getCupcakes() {

  let response = await
    axios.get(DEFAULT_URL + '/api/cupcakes');
  console.log('response.data.cupcakes=', response.data.cupcakes);
  return response.data.cupcakes;
}


function populatingCupcakes(cupcakes) {


  $cupcakes.empty();
  // let $li = $("<li>");
  for (let cupcake of cupcakes) {
    $cupcakes.append(`<li>
      ${cupcake.flavor}
      ${cupcake.size}
      ${cupcake.rating}
      <img src=${cupcake.image_url} alt=${cupcake.flavor}> </li>`);
  }

}


async function start() {

  let cupcakes = await getCupcakes();

  // populatingCupcakes(cupcakes);

}

start();