import React from 'react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>&copy; 2024 TodoApp. All rights reserved.</p>
        <div className="footer-links">
          <a href="/about">About</a>
          <a href="/how-it-works">How It Works</a>
          <a href="/contact">Contact</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;