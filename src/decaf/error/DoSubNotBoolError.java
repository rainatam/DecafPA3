package decaf.error;

import decaf.Location;

/**
 * example：array subscript must be an integer<br>
 * PA2
 */
public class DoSubNotBoolError extends DecafError {

    private String given;
    public DoSubNotBoolError(Location location, String given) {
        super(location);
        this.given = given;
    }

    @Override
    protected String getErrMsg() {
        return "The condition of Do Stmt requestd type bool but " + given + " given";
    }

}
