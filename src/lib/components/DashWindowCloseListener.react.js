import React, { Component } from 'react';
import PropTypes from 'prop-types';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class DashWindowCloseListener extends Component {
    constructor(props) {
        super(props);
        this.closeWindow = this.closeWindow.bind(this);
        this.setStatus = this.setStatus.bind(this);
        this.sendClosed = this.sendClosed.bind(this);


    }
    closeWindow() {
        this.setStatus("closing");
    }
    setStatus(status) {
        const { setProps } = this.props;
        const propsToChange = {};
        propsToChange.status = status;
        setProps(propsToChange);
    }
    sendClosed(e) {
        this.setStatus("closing");
    }
    componentDidMount() {
        this.setStatus("mounted");
        window.addEventListener('beforeunload', this.sendClosed);

    }
    componentWillUnmount() {
        window.removeEventListener('beforeunload', this.sendClosed);
    }
    render() {

        return (
            <div id={this.props.id}>
            </div>
        );
    }
}



DashWindowCloseListener.defaultProps = {
};

DashWindowCloseListener.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * The status of the window. Mounted or closing.
     */
    status: PropTypes.string,
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
