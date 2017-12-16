package decaf.error;

import decaf.Location;

public class ConditionNotUniqueError extends DecafError{

    public ConditionNotUniqueError(Location location) {
        super(location);
    }

    @Override
    protected String getErrMsg() {
        return "condition is not unique";
    }


}
