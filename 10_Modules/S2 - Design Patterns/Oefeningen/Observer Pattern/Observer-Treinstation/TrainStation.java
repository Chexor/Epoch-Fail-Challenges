import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;

public class TrainStation {

    private List<TrainObserver> observers = new ArrayList<>();
    private List<TrainEvent> events = new ArrayList<>();

    public void registerObserver(TrainObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(TrainObserver observer) {
        observers.remove(observer);
    }

    public void notifyObservers(TrainEvent event) {
        for (TrainObserver observer : observers) {
            observer.update(event);
        }
    }

    public void newArrival(String trainNumber, int trackNumber, LocalTime time) {
        TrainEvent event = new Arrival(trainNumber, trackNumber, time);
        events.add(event);
        notifyObservers(event);
    }

    public void newDeparture(String trainNumber, int trackNumber, LocalTime time) {
        TrainEvent event = new Departure(trainNumber, trackNumber, time);
        events.add(event);
        notifyObservers(event);
    }
}
