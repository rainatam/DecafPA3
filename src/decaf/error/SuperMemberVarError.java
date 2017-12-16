package decaf.error;

import decaf.Location;

public class SuperMemberVarError extends DecafError{
    public SuperMemberVarError(Location location) {
        super(location);
    }

    @Override
    protected String getErrMsg() {
        return "super.member_var is not supported";
    }

}
