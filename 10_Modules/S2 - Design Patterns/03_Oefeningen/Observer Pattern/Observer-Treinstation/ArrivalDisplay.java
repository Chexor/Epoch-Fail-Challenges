public class ArrivalDisplay implements TrainObserver {

    @Override
    public void update(TrainEvent event) {
        if ("Arrival".equals(event.getType())) {
            System.out.println("== AANKOMSTBORD ==\n" + event.toString() + "\n");
        }
    }
}
