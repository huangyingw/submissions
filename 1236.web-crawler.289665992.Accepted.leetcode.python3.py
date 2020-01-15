class Solution(object):
    def crawl(self, startUrl, htmlParser):
        PREFIX = "http://"
        n = len(PREFIX)

        def get_host_and_path(url):
            suffix = url[n:]
            if "/" not in suffix:
                return [suffix, ""]
            return suffix.split("/", 1)
        start_host, _ = get_host_and_path(startUrl)
        results = set()

        def dfs(url):
            if url in results:
                return
            host, path = get_host_and_path(url)
            if host != start_host:
                return
            results.add(url)
            for next_url in htmlParser.getUrls(url):
                dfs(next_url)
        dfs(startUrl)
        return list(results)
