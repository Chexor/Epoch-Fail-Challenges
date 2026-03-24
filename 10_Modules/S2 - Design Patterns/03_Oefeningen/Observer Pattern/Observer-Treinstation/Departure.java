import java.time.LocalTime;

public class Departure implements TrainEvent {
    private final String trainNumber;
    private final int trackNumber;
    private final LocalTime time;

    public Departure(String trainNumber, int trackNumber, LocalTime time) {
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
        return "Departure";
    }

    @Override
    public String toString() {
        return String.format("[VERTREK] Trein %s vertrekt om %s van spoor %d.", trainNumber, time, trackNumber);
    }
}
