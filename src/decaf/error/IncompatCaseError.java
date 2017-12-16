package decaf.error;
import decaf.Location;

/**
 * example：incompatible operand: - int[]<br>
 * PA2
 */
public class IncompatCaseError extends DecafError {

    private String givenType;

    private String expectedType;

    public IncompatCaseError(Location location, String givenType, String expectedType) {
        super(location);
        this.givenType = givenType;
        this.expectedType = expectedType;
    }

    @Override
    protected String getErrMsg() {
        return "incompatible case expr: " + givenType + " given, but " + expectedType + " expected";
    }

}
