from langchain_community.tools import DuckDuckGoSearchRun


def search_with_subject(subject):
    searched_result = ""
    try:
        search = DuckDuckGoSearchRun()
        searched_result = search.invoke(subject + " 나무위키")
        print(searched_result)
    except:
        searched_result = ""
    finally:
        return searched_result
