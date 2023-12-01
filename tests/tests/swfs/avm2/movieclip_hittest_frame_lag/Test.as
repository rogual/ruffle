package {
    import flash.display.*;
    import flash.events.*;

    public class Test extends MovieClip {
        public function Test() {
            this.addEventListener(Event.ENTER_FRAME, this.onEnterFrame);
        }

        private function onEnterFrame(e) {
            if (enemies.y == 0)
                enemies.y = 50
            else
                enemies.y = 0
            
            var hit = enemies.hitTestPoint(0, 0, true);
            trace(hit);
        }
    }
}
