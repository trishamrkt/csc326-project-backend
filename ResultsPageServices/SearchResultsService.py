import pprint
import math
import json

class SearchResultsService():

    def __init__(self, textData, pageRankData):
        self.__textData = textData;
        self.__pageRankData = pageRankData;

    def find_word(self, keyword):
        """
        4 Steps to finding the word:

            1. get list of urls which the word points to
            2. put url with its respective rank (in a dictionary)
                - create structure of url object:
                    {'url': '', 'title': '', 'description': ''}
            3. create dictionary with rank as key, and url object as its value
            4. compare the ranks to sort and put in new dictionary to return (sorted_urls)
        """
        sorted_urls = {};

        # Step 1
        urls = self.__textData.get_urls_from_word(keyword);

        if urls != None:
            # Step 2
            url_rank = {};
            for url in urls:
                rank = self.__pageRankData.get_page_rank(url);
                url_rank[url] = rank;

            # Step 3
            rank_url_obj = {};
            count = 0;
            for url, rank in url_rank.iteritems():

                url_obj = self.__get_url_obj(url);
                rank_url_obj[count] = dict({'rank': rank, 'url_obj': url_obj});
                count = count + 1;

            # Step 4
            for n in range(0, len(urls)):
                highest_url_obj = {};
                highest_rank = float(0);
                highest_num = 0;
                counter = 0;

                for num, obj in rank_url_obj.iteritems():
                    rank = obj['rank'];
                    url_obj = obj['url_obj'];

                    if counter == 0:
                        self.__deep_copy_dictionary(highest_url_obj, url_obj);
                        highest_rank = rank;
                        highest_num = num;
                    else:
                        if rank > highest_rank:
                            self.__deep_copy_dictionary(highest_url_obj, url_obj);
                            highest_rank = rank;
                            highest_num = num;


                    counter = counter + 1;

                if highest_rank != 0:
                    sorted_urls[n] = highest_url_obj;
                    del rank_url_obj[highest_num];

        return sorted_urls;

    # Splits the sorted urls into arrays of 5 to be passed back into the frontend
    def get_return_results(self, sorted_urls):
        # Array containing data for each search result page (ie arrays of 5)
        search_results = []

        num_results = len(sorted_urls)
        num_pages = math.ceil(num_results/5.0)

        # Keep track of how many results in a page
        result_count = 0
        # Array to go into search results (holds max of 5 url objects)
        results_per_page = []

        # Iterate through sorted urls and adds to each page array 
        for key, value in sorted_urls.iteritems():
            if result_count < 5:
                results_per_page.append(value)
                result_count += 1
            else:
                search_results.append(results_per_page)
                results_per_page = [value]
                result_count = 1

        if len(search_results) < num_pages:
            search_results.append(results_per_page)

        return search_results


    def __get_url_obj(self, url):
        title = self.__textData.get_title_from_url(url);
        desc = self.__textData.get_description_from_url(url);

        url_obj = dict(
                        {'url': url,
                         'title': title,
                         'desc': desc
                        });
        return url_obj

    def __deep_copy_dictionary(self, copy, src):
        copy['url'] = src['url'];
        copy['title'] = src['title'];
        copy['description'] = src['desc'];
