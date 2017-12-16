package decaf.error;
import decaf.Location;

/**
 * example：incompatible operand: - int[]<br>
 * PA2
 */
public class DifferentTypeError extends DecafError {

    private String givenType;

    private String expectedType;

    public DifferentTypeError(Location location, String givenType, String expectedType) {
        super(location);
        this.givenType = givenType;
        this.expectedType = expectedType;
    }

    @Override
    protected String getErrMsg() {
        return "type: " + givenType + " is different with other expr's type " + expectedType;
    }

}
