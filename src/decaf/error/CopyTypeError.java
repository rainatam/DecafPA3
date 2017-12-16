package decaf.error;

import decaf.Location;

public class CopyTypeError extends DecafError{
    private String given;

    public CopyTypeError(Location location, String given) {
        super(location);
        this.given = given;
    }

    @Override
    protected String getErrMsg() {
        return "expected class type for copy expr but " + given + " given";
    }

}
