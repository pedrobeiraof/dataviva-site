var occugrid = document.getElementById('occugrid')
    lang = document.documentElement.lang,
    cicles = occugrid.getAttribute('cicles'),
    size = occugrid.getAttribute('size'),
    group = occugrid.getAttribute('group'),
    dataset = occugrid.getAttribute('dataset'),

// Temporarily translates text until dictionary is updated
dictionary['state'] = lang == 'en' ? 'State' : 'Estado';
dictionary['municipality'] = lang == 'en' ? 'Municipality' : 'Municipio';
dictionary['section'] = lang == 'en' ? 'Section' : 'Seção';
dictionary['product'] = lang == 'en' ? 'Product' : 'Produto';
dictionary['product'] = lang == 'en' ? 'Product' : 'Produto';
dictionary['data_provided_by'] = lang == 'en' ? 'Data provided by' : 'Dados fornecidos por';
dictionary['by'] = lang == 'en' ? 'by' : 'por';
dictionary['of'] = lang == 'en' ? 'of' : 'de';
dictionary['port'] = lang == 'en' ? 'Port' : 'Porto';
dictionary['country'] = lang == 'en' ? 'Country' : 'País';
dictionary['continent'] = lang == 'en' ? 'Continent' : 'Continente';
dictionary['kg'] = 'KG';


var buildData = function(apiResponse) {

    var getAttrByName = function(item, attr) {
        var index = headers.indexOf(attr);
        return item[index];
    }

    var data = [];
    var headers = apiResponse.headers;

    apiResponse.data.forEach(function(item) {
        var dataItem = {};

        headers.forEach(function(header){   
            dataItem[header] = getAttrByName(item, header);
        });
        dataItem['main_group'] = dataItem['occupation'][0]
        data.push(dataItem);
    });

    return data;
}

var loadViz = function(data) {
  // instantiate d3plus
  var visualization = d3plus.viz()
    .container("#occugrid")     // container DIV to hold the visualization
    .data(data)     // data to use with the visualization
    .type("bubbles")       // visualization type
    .id("main_group") // nesting keys
    .size("jobs")         // key name to size bubbles
    .draw()                // finally, draw the visualization!

};

var loading = dataviva.ui.loading('.loading').text(dictionary['loading'] + '...');

$(document).ready(function() {
    var urls = ['http://api.staging.dataviva.info/rais/year/cnae/occupation/?value=jobs&cnae=14126&year=2014'];

    ajaxQueue(
        urls, 
        function(responses){
            var data = responses[0];             data = buildData(data);

            loading.hide();
            loadViz(data);
        })
});