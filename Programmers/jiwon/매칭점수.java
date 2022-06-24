import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class Solution {
    public static void main(String[] args) {

    }
    HashMap<String, Link> Links;

    public int solution(String word, String[] pages) {
        int answer = 0;
        Links = new HashMap<>();

        Pattern homeUrlPattern = Pattern.compile("<meta property=\"og:url\" content=\"(\\S*)\""); //자기 자신의 url 링크 추출
        Pattern urlPattern = Pattern.compile("<a href=\"https://(\\S*)\""); //외부 링크 추출
        Pattern wordPattern = Pattern.compile("\\b(?i)"+word+"\\b"); //단어 언급 수 (기본점수)
        Matcher urlMatcher, wordMatcher, homeUrlMatcher;

        ArrayList<String> extUrls;
        Link newLink;
        String body;
        String homeUrl = "";

        for(int i=0;i<pages.length;i++) {
            urlMatcher = urlPattern.matcher(pages[i]);
            homeUrlMatcher = homeUrlPattern.matcher(pages[i]);

            if(homeUrlMatcher.find()) {
                homeUrl = homeUrlMatcher.group().split("=")[2].replaceAll("\"", "");
            }

            newLink = new Link(i, homeUrl);
            extUrls = new ArrayList<>();

            while(urlMatcher.find()) {
                extUrls.add(urlMatcher.group().split("\"")[1]);
            }
            newLink.setExtUrls(extUrls);

            body = pages[i].split("<body>")[1].split("</body>")[0].replaceAll("[0-9]", " ");
            wordMatcher = wordPattern.matcher(body);
            int wordCnt = 0;
            while(wordMatcher.find()) {
                wordCnt++;
            }
            newLink.point = wordCnt;
            newLink.setLinkPoint();
            Links.put(newLink.url, newLink);
        }

        for(Link link: Links.values()){
            for(String extUrl : link.extUrls){
                if(Links.containsKey(extUrl)){
                    Links.get(extUrl).point += link.linkPoint;
                }
            }
        }

        double max_point = 0;
        for(Link link: Links.values()){
            if(link.point == max_point){
                if(link.index < answer)
                    answer = link.index;
            }
            else if(link.point > max_point) {
                answer = link.index;
                max_point = link.point;
            }
        }

        return answer;
    }

    class Link {
        String url; //자기 자신 링크
        String[] extUrls; //외부 링크들
        double point, linkPoint; //기본 점수, 링크 점수
        int index; //인덱스

        public Link(int index, String url) {
            this.index = index;
            this.url = url;
        }

        public void setExtUrls(ArrayList<String> urls) {
            this.extUrls = new String[urls.size()];
            for(int i=0; i<urls.size();i++) {
                extUrls[i] = urls.get(i);
            }
        }

        public void setLinkPoint() {
            this.linkPoint = this.point / extUrls.length;
        }
    }
}