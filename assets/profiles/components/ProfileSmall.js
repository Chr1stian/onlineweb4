import React from 'react';

class ProfileSmall extends React.Component {
  render() {
    const { image, name, phone, mail } = this.props.user;
    return (
      <div className="profile-small-container">
        <img className="profile-image" src={ image } title={ name }></img>
        <div className="profile-small-content">
          <p className="profile-small-name">{ name }</p>
          <p className="profile-info-type">E-post</p>
          <p className="profile-info-content">{ mail }</p>
          <p className="profile-info-type">Telefonnummer</p>
          <p className="profile-info-content">{ phone }</p>
        </div>
      </div>
    );
  }
}

export default ProfileSmall;