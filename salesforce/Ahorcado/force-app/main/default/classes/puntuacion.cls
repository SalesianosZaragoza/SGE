public with sharing class puntuacion {
    static List<List<String>> scoreboard = new List<List<String>>();

    public puntuacion() {

    }

    @AuraEnabled
    public static List<List<String>> addScoreboard(String tiempo, String intentos){
        List<String> score = new List<String>();

        score.add(tiempo);
        score.add(intentos);

        scoreboard.add(score);
        return scoreboard;
    }
}
