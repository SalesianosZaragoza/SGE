public with sharing class puntuacionController {
    static List<String> scoreList = new List<String>();
    @AuraEnabled
    public static List<String> getScoreList(String newScore, String[] scores ){
        scoreList = scores;
        scoreList.add(newScore);
        return scoreList;
    }
}

