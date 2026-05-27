// DOM Elements and State
let animatedCounters = [];
let animatedBars = [];
let hasAnimated = false;
let plateauAnimated = false;

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing...');
    initializeIntersectionObserver();
    initializeRevealCards();
    initializeCTAButtons();
    initializeShareButtons();
    initializeProgressBars();
    setupScrollAnimations();
});

// Intersection Observer for scroll-triggered animations
function initializeIntersectionObserver() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.classList.contains('stats-dashboard') && !hasAnimated) {
                    animateCounters();
                }
                if (entry.target.classList.contains('comparison-section')) {
                    animateProgressBars();
                }
                if (entry.target.classList.contains('plateau-section') && !plateauAnimated) {
                    animatePlateauCounters();
                }
                
                // Add slide-in animation
                entry.target.classList.add('animate-in');
            }
        });
    }, {
        threshold: 0.2,
        rootMargin: '50px'
    });

    // Observe key sections
    const sections = document.querySelectorAll('.stats-dashboard, .comparison-section, .plateau-section, .reveal-sections');
    sections.forEach(section => observer.observe(section));
}

// Animated counters for statistics
function animateCounters() {
    if (hasAnimated) return;
    hasAnimated = true;
    console.log('Starting counter animations...');

    const counters = document.querySelectorAll('.stat-number[data-target]');
    
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000; // 2 seconds
        const step = target / (duration / 16); // 60fps
        let current = 0;
        
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            counter.textContent = Math.floor(current);
        }, 16);
        
        // Add a subtle bounce effect when complete
        setTimeout(() => {
            counter.style.transform = 'scale(1.1)';
            counter.style.transition = 'transform 0.2s ease';
            setTimeout(() => {
                counter.style.transform = 'scale(1)';
            }, 200);
        }, duration);
    });
}

// Animated counters for plateau section
function animatePlateauCounters() {
    if (plateauAnimated) return;
    plateauAnimated = true;
    console.log('Starting plateau counter animations...');

    const plateauCounters = document.querySelectorAll('.big-number[data-target]');
    
    plateauCounters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 1500;
        const step = target / (duration / 16);
        let current = 0;
        
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            counter.textContent = Math.floor(current);
        }, 16);
    });
}

// Progress bar animations
function initializeProgressBars() {
    const progressBars = document.querySelectorAll('.progress-fill[data-width]');
    progressBars.forEach(bar => {
        bar.style.width = '0%';
    });
}

function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-fill[data-width]');
    
    progressBars.forEach((bar, index) => {
        const targetWidth = bar.getAttribute('data-width');
        
        setTimeout(() => {
            bar.style.width = targetWidth + '%';
            
            // Add a glow effect for critical bars
            if (bar.closest('.critical-bar')) {
                setTimeout(() => {
                    bar.style.boxShadow = '0 0 15px rgba(255, 84, 89, 0.5)';
                }, 1000);
            }
        }, index * 200);
    });
}

// Reveal cards functionality - FIXED
function initializeRevealCards() {
    console.log('Initializing reveal cards...');
    const revealCards = document.querySelectorAll('.reveal-card');
    console.log('Found reveal cards:', revealCards.length);
    
    revealCards.forEach((card, index) => {
        const header = card.querySelector('.reveal-header');
        const content = card.querySelector('.reveal-content');
        const expandIcon = card.querySelector('.expand-icon');
        
        if (!header || !content) {
            console.error('Missing header or content for card', index);
            return;
        }
        
        // Ensure proper initial state
        card.classList.remove('expanded');
        content.style.maxHeight = '0';
        content.style.overflow = 'hidden';
        
        header.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Reveal card clicked:', index);
            
            const isExpanded = card.classList.contains('expanded');
            
            // Close all other cards first
            revealCards.forEach(otherCard => {
                if (otherCard !== card) {
                    otherCard.classList.remove('expanded');
                    const otherContent = otherCard.querySelector('.reveal-content');
                    const otherIcon = otherCard.querySelector('.expand-icon');
                    if (otherContent) otherContent.style.maxHeight = '0';
                    if (otherIcon) otherIcon.textContent = '+';
                }
            });
            
            // Toggle current card
            if (isExpanded) {
                card.classList.remove('expanded');
                content.style.maxHeight = '0';
                expandIcon.textContent = '+';
                console.log('Card collapsed');
            } else {
                card.classList.add('expanded');
                content.style.maxHeight = '200px';
                expandIcon.textContent = '×';
                console.log('Card expanded');
                
                // Track engagement
                trackEvent('reveal_section_opened', {
                    section: header.querySelector('h3').textContent
                });
            }
        });
        
        // Add hover effects
        header.addEventListener('mouseenter', () => {
            if (!card.classList.contains('expanded')) {
                card.style.transform = 'translateY(-2px)';
                card.style.transition = 'transform 0.2s ease';
            }
        });
        
        header.addEventListener('mouseleave', () => {
            if (!card.classList.contains('expanded')) {
                card.style.transform = 'translateY(0)';
            }
        });
    });
}

// CTA Button functionality - FIXED
function initializeCTAButtons() {
    console.log('Initializing CTA buttons...');
    const ctaButtons = document.querySelectorAll('.cta-btn');
    console.log('Found CTA buttons:', ctaButtons.length);
    
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('CTA button clicked');
            
            const action = button.getAttribute('data-action');
            console.log('Action:', action);
            
            handleCTAAction(action);
            
            // Add click animation
            button.style.transform = 'scale(0.95)';
            button.style.transition = 'transform 0.15s ease';
            setTimeout(() => {
                button.style.transform = 'scale(1)';
            }, 150);
        });
    });
}

// Handle CTA actions - FIXED
function handleCTAAction(action) {
    console.log('Handling CTA action:', action);
    
    switch(action) {
        case 'report':
            showModal('report-modal');
            trackEvent('cta_clicked', { action: 'download_report' });
            break;
            
        case 'consultation':
            showModal('consultation-modal');
            trackEvent('cta_clicked', { action: 'book_consultation' });
            break;
            
        default:
            console.log('Unknown action:', action);
    }
}

// Share button functionality - FIXED
function initializeShareButtons() {
    console.log('Initializing share buttons...');
    const shareButtons = document.querySelectorAll('.share-btn');
    console.log('Found share buttons:', shareButtons.length);
    
    shareButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Share button clicked');
            
            const platform = button.getAttribute('data-platform');
            console.log('Platform:', platform);
            
            handleShare(platform);
            
            // Add share animation
            button.style.background = 'rgba(255, 255, 255, 0.3)';
            button.style.transition = 'background 0.2s ease';
            setTimeout(() => {
                button.style.background = 'rgba(255, 255, 255, 0.1)';
            }, 200);
        });
    });
}

// Handle sharing - FIXED
function handleShare(platform) {
    console.log('Handling share for platform:', platform);
    
    const title = "WA's $146B AI Crisis: Why 76% of SMEs Are Stuck in the Digital Stone Age";
    const text = "Shocking data reveals WA SMEs are falling dangerously behind in AI adoption. See the devastating comparison with the rest of Australia.";
    const url = window.location.href;
    
    let shareUrl = '';
    
    switch(platform) {
        case 'linkedin':
            shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`;
            break;
            
        case 'twitter':
            shareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text + ' ' + url)}`;
            break;
            
        case 'email':
            shareUrl = `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(text + '\n\n' + url)}`;
            break;
    }
    
    if (shareUrl) {
        console.log('Opening share URL:', shareUrl);
        window.open(shareUrl, '_blank', 'width=600,height=400');
        trackEvent('content_shared', { platform: platform });
        showNotification(`Sharing on ${platform.charAt(0).toUpperCase() + platform.slice(1)}...`, 'success');
    }
}

// Scroll-triggered animations
function setupScrollAnimations() {
    const cards = document.querySelectorAll('.stat-card, .comparison-card, .stage-card');
    
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '50px'
    });
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease-out';
        cardObserver.observe(card);
    });
}

// Show modal - FIXED
function showModal(modalId) {
    console.log('Showing modal:', modalId);
    
    // Remove any existing modals
    const existingOverlay = document.querySelector('.modal-overlay');
    if (existingOverlay) {
        existingOverlay.remove();
    }
    
    // Create modal overlay
    const overlay = document.createElement('div');
    overlay.className = 'modal-overlay';
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        animation: fadeIn 0.3s ease-out;
    `;
    
    const modal = document.createElement('div');
    modal.className = 'modal-content';
    modal.style.cssText = `
        background: var(--color-surface);
        padding: var(--space-32);
        border-radius: var(--radius-lg);
        max-width: 500px;
        width: 90%;
        text-align: center;
        animation: slideInUp 0.3s ease-out;
        box-shadow: var(--shadow-lg);
    `;
    
    const content = modalId === 'report-modal' 
        ? `
            <h3 style="color: var(--color-text); margin-bottom: var(--space-16); font-size: var(--font-size-2xl);">📊 Download Full AI Strategy Report</h3>
            <p style="color: var(--color-text-secondary); margin-bottom: var(--space-24); line-height: 1.5;">Get comprehensive insights into WA's AI adoption crisis and strategic recommendations for your business.</p>
            <div style="display: flex; gap: var(--space-16); justify-content: center; flex-wrap: wrap;">
                <button class="btn btn--primary modal-action" data-modal-action="download">Download Now</button>
                <button class="btn btn--outline modal-action" data-modal-action="close">Cancel</button>
            </div>
        `
        : `
            <h3 style="color: var(--color-text); margin-bottom: var(--space-16); font-size: var(--font-size-2xl);">📞 Book AI Strategy Session</h3>
            <p style="color: var(--color-text-secondary); margin-bottom: var(--space-24); line-height: 1.5;">Schedule a consultation to develop your AI roadmap and close the competitive gap.</p>
            <div style="display: flex; gap: var(--space-16); justify-content: center; flex-wrap: wrap;">
                <button class="btn btn--primary modal-action" data-modal-action="book">Book Session</button>
                <button class="btn btn--outline modal-action" data-modal-action="close">Cancel</button>
            </div>
        `;
    
    modal.innerHTML = content;
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
    
    // Add modal action handlers
    const modalActions = modal.querySelectorAll('.modal-action');
    modalActions.forEach(actionBtn => {
        actionBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const action = this.getAttribute('data-modal-action');
            
            if (action === 'download') {
                showNotification('Report download started! Check your downloads folder.', 'success');
                trackEvent('report_downloaded');
            } else if (action === 'book') {
                showNotification('Redirecting to booking calendar...', 'info');
                trackEvent('consultation_booked');
            }
            
            closeModal();
        });
    });
    
    // Close on overlay click
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            closeModal();
        }
    });
    
    // Add ESC key handler
    const escHandler = (e) => {
        if (e.key === 'Escape') {
            closeModal();
            document.removeEventListener('keydown', escHandler);
        }
    };
    document.addEventListener('keydown', escHandler);
    
    // Store reference for closing
    window.currentModal = overlay;
}

function closeModal() {
    console.log('Closing modal');
    const overlay = document.querySelector('.modal-overlay');
    if (overlay) {
        overlay.style.animation = 'fadeOut 0.3s ease-out';
        setTimeout(() => {
            if (overlay.parentNode) {
                overlay.parentNode.removeChild(overlay);
            }
        }, 300);
    }
    window.currentModal = null;
}

function showNotification(message, type = 'info') {
    console.log('Showing notification:', message, type);
    
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    
    const bgColor = type === 'success' ? 'var(--color-success)' : 
                    type === 'error' ? 'var(--color-error)' : 
                    'var(--color-primary)';
    
    notification.style.cssText = `
        position: fixed;
        top: var(--space-20);
        right: var(--space-20);
        background: var(--color-surface);
        color: var(--color-text);
        padding: var(--space-16) var(--space-20);
        border-radius: var(--radius-base);
        box-shadow: var(--shadow-lg);
        z-index: 10001;
        border-left: 4px solid ${bgColor};
        animation: slideInRight 0.3s ease-out;
        max-width: 300px;
        font-size: var(--font-size-sm);
    `;
    
    notification.textContent = message;
    document.body.appendChild(notification);
    
    // Auto-remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => {
            if (document.body.contains(notification)) {
                document.body.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Analytics tracking (placeholder)
function trackEvent(eventName, properties = {}) {
    // In a real application, this would send to analytics service
    console.log('Event tracked:', eventName, properties);
}

// Add CSS animations dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes fadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
    }
    
    @keyframes slideInUp {
        from { 
            opacity: 0; 
            transform: translateY(50px); 
        }
        to { 
            opacity: 1; 
            transform: translateY(0); 
        }
    }
    
    @keyframes slideInRight {
        from { 
            opacity: 0; 
            transform: translateX(100%); 
        }
        to { 
            opacity: 1; 
            transform: translateX(0); 
        }
    }
    
    @keyframes slideOutRight {
        from { 
            opacity: 1; 
            transform: translateX(0); 
        }
        to { 
            opacity: 0; 
            transform: translateX(100%); 
        }
    }
    
    .modal-action {
        cursor: pointer;
    }
    
    .reveal-header {
        cursor: pointer;
        user-select: none;
    }
    
    .expand-icon {
        cursor: pointer;
        user-select: none;
        font-family: monospace;
        font-size: var(--font-size-2xl);
        line-height: 1;
    }
`;
document.head.appendChild(style);

// Add smooth scrolling for better UX
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading state management
window.addEventListener('load', () => {
    console.log('Window loaded');
    document.body.classList.add('loaded');
    
    // Trigger initial animations
    const heroElements = document.querySelectorAll('.hero-title, .hero-subtitle, .hero-stats-preview');
    heroElements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'all 0.8s ease-out';
        
        setTimeout(() => {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 200);
    });
});

// Handle visibility change for performance
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        // Pause animations when tab is not visible
        document.body.classList.add('paused');
    } else {
        // Resume animations when tab becomes visible
        document.body.classList.remove('paused');
    }
});

// Error handling for better UX
window.addEventListener('error', (e) => {
    console.error('Application error:', e.error);
    showNotification('An error occurred. Please refresh the page.', 'error');
});

// Add focus management for accessibility
document.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
        document.body.classList.add('keyboard-navigation');
    }
});

document.addEventListener('mousedown', () => {
    document.body.classList.remove('keyboard-navigation');
});