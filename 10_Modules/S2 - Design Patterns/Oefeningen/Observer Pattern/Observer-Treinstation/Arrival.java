import java.time.LocalTime;

public class Arrival implements TrainEvent {
    private final String trainNumber;
    private final int trackNumber;
    private final LocalTime time;

    public Arrival(String trainNumber, int trackNumber, LocalTime time) {
        this.trainNumber = trainNumber;
        this.trackNumber = trackNumber;
        this.time = time;
    }

    @Override
    public String getTrainNumber() {
        return trainNumber;
    }

    @Override
    public int getTrackNumber() {
        return trackNumber;
    }

    @Override
    public LocalTime getTime() {
        return time;
    }

    @Override
    public String getType() {
        return "Arrival";
    }
    
    @Override
    public String toString() {
        return String.format("[AANKOMST] Trein %s komt aan om %s op spoor %d.", trainNumber, time, trackNumber);
    }
}
