google.load('visualization', '1', {packages: ['corechart', 'bar']});
google.setOnLoadCallback(drawBasic);

function drawBasic() {

    var data = google.visualization.arrayToDataTable([
        ['Police Rank', 'Number of Police in Rank',],
        {% for rank_number in rank_number %}
            ['{{ rank_number.rank_name }}', {{ rank_number.NumberOfficers }}],
        {% endfor %}
        ]);

    var options = {
        title: 'How many police per rank',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Number of Officers in Rank',
            minValue: 0
        },
        vAxis: {
            title: 'Police Rank'
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('police_rank_chart'));

    chart.draw(data, options);
}
