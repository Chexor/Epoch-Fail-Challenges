public class GeneralDisplay implements TrainObserver {

    @Override
    public void update(TrainEvent event) {
        System.out.println("== ALGEMEEN BORD ==\n" + event.toString() + "\n");
    }
}
