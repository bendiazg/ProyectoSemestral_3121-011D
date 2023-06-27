const URL='https://dog.ceo/api/breeds/'+
                            'image/random';
fetch(URL)
    .then(response=>response.json())
    .then(data=>imgDog.src=data.message);