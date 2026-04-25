public class DepartureDisplay implements TrainObserver {

    @Override
    public void update(TrainEvent event) {
        if ("Departure".equals(event.getType())) {
            System.out.println("== VERTREKBORD ==\n" + event.toString() + "\n");
        }
    }
}
