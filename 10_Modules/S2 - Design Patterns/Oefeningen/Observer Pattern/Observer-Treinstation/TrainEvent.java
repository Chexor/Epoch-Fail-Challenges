package OefeningObserverTreinstation;

import java.time.LocalTime;

public interface TrainEvent {
    String getTrainNumber();
    int getTrackNumber();
    LocalTime getTime();
    String getType();
}
