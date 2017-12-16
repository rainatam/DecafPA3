package decaf.error;

import decaf.Location;

public class CopySrcDstNotSameError extends DecafError {
    private String src, dst;

    public CopySrcDstNotSameError(Location location, String src, String dst) {
        super(location);
        this.src = src;
        this.dst = dst;
    }

    @Override
    protected String getErrMsg() {
        return "For copy expr, the source " + src + " and the destination " + dst + " are not same";
    }

}
