import React, { useState, useEffect } from 'react';
import './BackToTopButton.css';

const BackToTopButton = () => {
  const [showBackToTop, setShowBackToTop] = useState(false);

  const handleScroll = () => {
    if (window.scrollY > 200) { // Show button after scrolling 200px
      setShowBackToTop(true);
    } else {
      setShowBackToTop(false);
    }
  };

  const handleScrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <>
      {showBackToTop && (
        <button className="back-to-top" onClick={handleScrollToTop}>
          &#9650; {/* Unicode for an upward-pointing triangle */}
        </button>
      )}
    </>
  );
};

export default BackToTopButton;