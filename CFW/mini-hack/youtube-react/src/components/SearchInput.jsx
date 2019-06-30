import React from 'react';

export const SearchInput = (props) => {
    return (
        <div className="row">
            <div className="col-md-12 text-center">
                <form id="search">
                    <div className="form-group">
                        <input placeholder='Find something on Youtube'
                            type="text" 
                            name="keyword" 
                            id="keyword" 
                            className="form-control" 
                            required
                            onChange={(e) => {
                                props.handleInputChange(e.target.value);
                            }} />
                        <input type="submit" className="btn btn-primary form-control" value="Submit"/> 
                    </div>
                </form>
            </div>
        </div>
    )
}