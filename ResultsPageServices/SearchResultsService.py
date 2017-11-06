import pprint

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
            for url, rank in url_rank.iteritems():
                url_obj = self.__get_url_obj(url);               
                rank_url_obj[rank] = url_obj;
    
            # Step 4
            for n in range(0, len(urls)):
                highest_url_obj = {};
                highest_rank = float(0);
                counter = 0;
    
                for rank, url_obj in rank_url_obj.iteritems():
                    if counter == 0:
                        self.__deep_copy_dictionary(highest_url_obj, url_obj);
                        highest_rank = rank;
                    else:
                        if rank > highest_rank:
                            self.__deep_copy_dictionary(highest_url_obj, url_obj);
                            highest_rank = rank;
                            
                    counter = counter + 1;
                            
                if highest_rank != 0:
                    sorted_urls[n] = highest_url_obj;
                    del rank_url_obj[highest_rank];

        return sorted_urls;
    
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
    