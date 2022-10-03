from streamlit_elements_fluence.core.frame import new_frame as _new_frame
from streamlit_elements_fluence.core.exceptions import *
from streamlit_elements_fluence.modules import *
from streamlit_elements_fluence.version import __version__
from streamlit_elements_fluence.core.jscallback import JSCallback


def elements(key: str) -> None:
    """Create a Streamlit Elements frame."""
    return _new_frame(key)
