function getBathElement() {
    var Bath_element = document.getElementsByName("Bath_element");
    for(var i in Bath_element) {
        if(Bath_element[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}

function getBedroomElement() {
    var Bedroom_element = document.getElementsByName("Bedroom_element");
    for(var i in Bedroom_element) {
        if(Bedroom_element[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}

function result(){
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("Sqft_element");         
    console.log("Got sqft: " + sqft.value);

    var lot_size = document.getElementById("lot_size_element");
    console.log("Got lot_size: " + lot_size.value);

    var bedrooms = getBedroomElement();
    console.log("Got bedrooms: " + bedrooms );

    var bathrooms = getBathElement();
    console.log("Got bathrooms: " + bathrooms);
    var city = document.getElementById("cities_element");
    console.log("Got city: " + city.value);
    var zip_code = document.getElementById("zip_code_element");
    console.log("Got zip code: " + zip_code.value);
    var price = document.getElementById("Estimated_price_element");
    console.log("Got price: " + price.value);

    
    var url = "http://127.0.0.1:5000/predict_home_price";
    $.post(url, {
        city: city.value,
        bedroom: bedrooms,
        bath: bathrooms,
        acre_lot: lot_size.value,
        zip_code:zip_code.value,
        sqft: parseFloat(sqft.value),
        
    }, function(data, status) {
        console.log(data)
        console.log(data.estimate_price);
        price.innerHTML = "<h2> $" + data.estimate_price.toString() +"</h2>";
        console.log(status);
    });
}

function onLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_cities";
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var cities = data.cities;
            var cities_element = document.getElementById("cities_element");
            $('#cities_element').empty();
            for (var i in cities) {
                var opt = new Option(cities[i]);
                $('#cities_element').append(opt);
            }
        }
    });
}

window.onload = onLoad;