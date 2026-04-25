import java.time.LocalTime;

public class Main {
    public static void main(String[] args) {
        // 1. Maak de Subject aan
        TrainStation station = new TrainStation();

        // 2. Maak de Observers aan
        TrainObserver generalDisplay = new GeneralDisplay();
        TrainObserver arrivalDisplay = new ArrivalDisplay();
        TrainObserver departureDisplay = new DepartureDisplay();

        // 3. Registreer de Observers bij de Subject
        station.registerObserver(generalDisplay);
        station.registerObserver(arrivalDisplay);
        station.registerObserver(departureDisplay);

        System.out.println("--- Simulatie gestart ---");

        // 4. Simuleer gebeurtenissen
        station.newArrival("IC123", 4, LocalTime.of(10, 30));
        station.newDeparture("THA987", 2, LocalTime.of(10, 35));
        station.newArrival("R456", 1, LocalTime.of(10, 42));

        System.out.println("\n--- Een display wordt verwijderd (ArrivalDisplay) ---");
        station.removeObserver(arrivalDisplay);

        station.newDeparture("IC555", 3, LocalTime.of(11, 0));

        System.out.println("\n--- Simulatie voltooid ---");
    }
}
