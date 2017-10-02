from bottle import *
from crawlerservice.CrawlerService import *
from toptwenty.toptwenty import TopTwenty
from toptwenty.word_data import WordData

crawlerService = CrawlerService();
most_popular = TopTwenty();

# Returns HTML for results page 
def word_count():
    search_string = request.query['keywords'].lower();
    word_data = WordData();

    # Gets HTML for table with words and their word counts
    html = '<link type="text/css" rel="stylesheet" href="/static/css/word_table_data.css"\>'
    html += "<link href='https://fonts.googleapis.com/css?family=Assistant' rel='stylesheet'>"
    html += '<nav class="navi"><a href="/">Googao</a></nav>'
    html = html + word_data.get_table_html(search_string.strip(), most_popular);
    html = html + most_popular.get_table_html();
    return html;

@route('/')
def root_path():
    if request.query_string == '':
        return template('index')
    else:
        return word_count();


@get('/static/css/<filepath:re:.*\.css>')
def static(filepath):
    return static_file(filepath, root='static/css')

run(host='localhost', port=8000, debug=True);
